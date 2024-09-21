select
f1.id, f2.id
from facebook_employees f1
inner join facebook_employees f2
on f1.location = f2.location
and f1.age <> f2.age
and f1.gender = f2.gender
and f1.is_senior <> f2.is_senior