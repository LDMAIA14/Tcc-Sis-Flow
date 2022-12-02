import { METHODS } from "http";
import React, { useState } from "react";
import getURL from "../../utils/getURL";
import{
    Container
}
from "./styles";

interface IFormProps{
    onSubit():void;
}

const Form : React.FC<IFormProps> = (({onSubit})=>{
    const [sigla,setSigla] = useState('');
    const [descricao,setDescricao] = useState('');
    const [tag_ft,setTag_FT] = useState('');
    const [tag_pt,setTag_PT] = useState('');
    async function insertNewZP(){
        const URL = getURL('zonaspressao');
        let body = {sigla:sigla,
            descricao:descricao,
            tag_ft:tag_ft,
            tag_pt:tag_pt};
        const response = await window.fetch(URL, {
            method: 'POST',
            headers: {
            'content-type': 'application/json',
            },
            body: JSON.stringify(body),
        })
        onSubit();
    }
    return(
        
        <Container onSubmit={e=>{
            e.preventDefault();    
            insertNewZP();
            
        }
        } id='myform'>
            <h2>Cadastro</h2>
            <input required type="text" name="" id="sigla" placeholder="Sigla" onChange={(e)=> setSigla(e.target.value)}/>
            <input required type="text" name="" id="descricao" placeholder="Descrição" onChange={(e)=> setDescricao(e.target.value)}/>
            <input required type="text" name="" id="tag_ft" placeholder="Tag Instrumento de Vazão" onChange={(e)=> setTag_FT(e.target.value)}/>
            <input required type="text" name="" id="tag_pt" placeholder="Tag Instrumento de Pressão" onChange={(e)=> setTag_PT(e.target.value)}/>
            <input  type="submit" value="Enviar" id="Btn"/>
        </Container>
    )


}
);
  


export default Form;