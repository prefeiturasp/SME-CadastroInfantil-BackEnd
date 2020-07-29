SELECT DISTINCT sg_dre, nm_dre
from "CI_cep_distrito_dre";

BEGIN;

select *
from "CI_cep_distrito_dre"
where nm_distrito like 'JARDIM ANGELA';

update "CI_cep_distrito_dre"
set sg_dre = 'CL',
    nm_dre = 'CAMPO LIMPO'
where nm_distrito like 'JARDIM ANGELA';

---------------------------------------------
select *
from "CI_cep_distrito_dre"
where nm_distrito like 'CAMPO GRANDE';

update "CI_cep_distrito_dre"
set sg_dre = 'SA',
    nm_dre = 'SANTO AMARO'
where nm_distrito like 'CAMPO GRANDE';
--------------------------------------
select *
from "CI_cep_distrito_dre"
where nm_distrito like 'ITAQUERA';

update "CI_cep_distrito_dre"
set sg_dre = 'IQ',
    nm_dre = 'ITAQUERA'
where nm_distrito like 'ITAQUERA';

--------------------------------------
select *
from "CI_cep_distrito_dre"
where nm_distrito like 'BRASILANDIA';

update "CI_cep_distrito_dre"
set sg_dre = 'FB',
    nm_dre = 'FREGUESIA-BRASILANDIA'
where nm_distrito like 'BRASILANDIA';

--------------------------------------
select *
from "CI_cep_distrito_dre"
where nm_distrito like 'ARTUR ALVIM';

update "CI_cep_distrito_dre"
set sg_dre = 'PE',
    nm_dre = 'PENHA'
where nm_distrito like 'ARTUR ALVIM';


-- COMMIT ;

ROLLBACK;