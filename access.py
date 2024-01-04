# if userid:
#             query = f'''
#                     SELECT
#                         pm.descr
#                     FROM
#                         general.active_product_grants apg
#                     INNER JOIN
#                         erp.product_master pm using(product_id)
#                     INNER JOIN
#                         general.gd_subscribers gs using(grant_id)
#                     WHERE
#                        apg. userid = {userid}
#                     AND
#                         pm.descr in('GD Starter', 'GD Max', 'GD Gold')
#                 '''
            
#             membership_plan = pg_conn.execute(text(query)).fetchone()
#             if membership_plan:
#                 membership_plan = membership_plan[0]
#             else:
#                 membership_plan = ''
#             total_count = 0
#             membership_plan = 'GD Starter'
#             if membership_plan=='GD Starter':
#                 total_count = 5
            
#             elif membership_plan=='GD Max':
#                 total_count = 15
#             elif membership_plan=='GD Gold':
#                 total_count = 25

#             hit_count = pg_conn.execute(text(f"select hit_count as count from general.gd_paid_member")).fetchone()
#             print(f"hhhhhhhhhhhhhhhh{hit_count}")
#             hit_count = hit_count[0] if hit_count else 0
#             print(f"hhhhhhhhhhhhhhhh====={hit_count}")
#             print(f"total_count=={total_count}==membership_plan=={membership_plan}==hit_count = {hit_count}")
#             uniq_id_exist = pg_conn.execute(text(f"SELECT 1 FROM general.gd_paid_member WHERE uniq_id @> Array[{int(uniq_id)}]")).fetchone()
#             print(f"uniq_id_exist=={uniq_id_exist}")
            
#             created_at = 0
#             if hit_count <= total_count and membership_plan and not uniq_id_exist:
#                 try :
#                     hit_count +=1
#                     print(222222222,hit_count,total_count,uniq_id_exist)

#                     with atomic() as txn:
#                         update_query = txn.custom_cursor(text(f'''
#                             Update 
#                                 general.gd_paid_member 
#                             set 
#                                 hit_count  = {hit_count} ,
#                                 updated_at = {int(datetime.now().timestamp())},
#                                 uniq_id = array_append(uniq_id, '{uniq_id}')
#                             where
#                                 gd_plan = '{membership_plan}' and userid = {userid}
#                             returning *
#                         '''))
#                         gd_paid_member_obj = update_query.mappings().fetchone()
#                         created_at = gd_paid_member_obj.get('created_at',0) if gd_paid_member_obj else 0
#                         if not created_at:
#                             hit_count = 0
#                 except Exception as e:
#                     raise Exception("Error in updation of hit count in gd paid member")
            

#             # difference_in_days =  int((int(datetime.now().timestamp())-1700032074)/ (60 * 60 * 24))
#             # print(f"difference_in_days=={difference_in_days}")

#             difference_in_days = pg_conn.execute(f"select to_timestamp(updated_at)::date-to_timestamp(created_at)::date as days from general.gd_paid_member where userid = {userid}").fetchone()
#             difference_in_days = difference_in_days[0] if difference_in_days else 0
#             print(f"difference_in_days=={difference_in_days}")
#             if (difference_in_days)==7:
#                 return JSONResponse({"msg":"Sorry you've exceeded the limit"}, status_code=200)
            
#             if hit_count>total_count and difference_in_days<7:
#                 return JSONResponse({"msg":"Sorry you've exceeded the limit111"}, status_code=200)
 
#             if hit_count>total_count and difference_in_days>7:
#                 with atomic() as txn:
#                         print(33333333)
#                         update_query = txn.custom_cursor(text(f'''
#                             Update 
#                                 general.gd_paid_member 
#                             set 
#                                 hit_count  = 0 ,
#                                 uniq_id = ARRAY[]::integer[],
#                                 updated_at =  {int(datetime.now().timestamp())},
#                                 created_at = {int(datetime.now().timestamp())}                                                            
#                             where
#                                 gd_plan = '{membership_plan}' and userid = {userid}
#                         '''))

#             if membership_plan and not hit_count:
#                 print(111111)
#                 try:
#                     with atomic(pg_conn =pg_conn) as conn:
#                         conn.custom_cursor(text(
#                             """
#                                 insert into general.gd_paid_member (userid,gd_plan,hit_count,uniq_id) VALUES(:userid ,:gd_plan,:hit_count,:uniq_id)
#                             """),dict(userid=  userid ,gd_plan = membership_plan, hit_count = 1, uniq_id = [int(uniq_id)])
#                         )
#                 except Exception as e:
#                     pass
