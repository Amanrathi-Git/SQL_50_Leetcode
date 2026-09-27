# Write your MySQL query statement below
select s.student_id , s.student_name , sub.subject_name , count(e.subject_name) as attended_exams
from Students s
cross join Subjects sub #cross when we want all data from both table
left join Examinations e
on s.student_id = e.student_id
and sub.subject_name = e.subject_name
group by s.student_id , s.student_name , sub.subject_name
order by s.student_id , s.student_name