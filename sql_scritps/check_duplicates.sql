select nome_crianca,
       sexo_crianca,
       nacionalidade_crianca,
       dt_entrada_brasil,
       dt_nasc_crianca,
       uf_nasc_crianca,
       municipio_nasc_crianca,
       raca_cor_crianca,
       tem_nee,
       tipo_nee,
       filiacao1_nome,
       filiacao1_falecido,
       filiacao1_sexo,
       filiacao1_nacionalidade,
       filiacao2_consta,
       filiacao2_nome,
       filiacao2_falecido,
       filiacao2_sexo,
       filiacao2_nacionalidade,
       cep_moradia,
       endereco_moradia,
       numero_moradia,
       complemento_moradia,
       tipo_responsavel,
       nome_responsavel,
       cpf_responsavel,
       dt_nasc_responsavel,
       email_responsavel,
       telefone_responsavel,
       parentesco_responsavel,
       telefone_opcional,
       irmao_na_rede,
       nome_irmao,
       count(1)
from "CI_solicitacao" sol
         inner join "CI_dados_crianca" Cdc on sol.dados_id = Cdc.id
group by nome_crianca, sexo_crianca, nacionalidade_crianca, dt_entrada_brasil, dt_nasc_crianca, uf_nasc_crianca,
         municipio_nasc_crianca, raca_cor_crianca, tem_nee, tipo_nee, filiacao1_nome, filiacao1_falecido,
         filiacao1_sexo, filiacao1_nacionalidade, filiacao2_consta, filiacao2_nome, filiacao2_falecido,
         filiacao2_sexo,
         filiacao2_nacionalidade, cep_moradia, endereco_moradia, numero_moradia, complemento_moradia,
         tipo_responsavel,
         nome_responsavel, cpf_responsavel, dt_nasc_responsavel, email_responsavel, telefone_responsavel,
         parentesco_responsavel, telefone_opcional, irmao_na_rede, nome_irmao
having count(1) > 1;

select *
from "CI_dados_crianca" dc
         inner join "CI_solicitacao" Cs on dc.id = Cs.dados_id
where dc.nome_crianca like 'THEO BISPO SOARES'