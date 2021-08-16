SELECT
    Firstname
    , Lastname
    , City
    , State
FROM
    Person AS p
    LEFT JOIN Address AS a -- using outer join is cruicial since not every person in Person table may have an address
    ON p.Personid = a.Personid
;