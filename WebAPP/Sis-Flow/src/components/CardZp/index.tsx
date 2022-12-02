import React, {useEffect, useMemo, useState} from "react";
import getURL from "../../utils/getURL";

import { Container, 
    Tag } 
from "./styles";


interface ICardZpProps{
   
    tagColor : boolean;
    sigla:string;
    descricao:string;
    tag_ft: string;
    tag_pt: string;
    id:string;
    onClick():void;
}

const CardZp : React.FC<ICardZpProps> = (
    {id,
    tagColor ,
    sigla,
    descricao,
    tag_ft,
    tag_pt,
    onClick}
    ) => {
    
   
    
    let tagColorStr = ''
    if(tagColor===true){
        tagColorStr = 'red'
    }else{
        tagColorStr = 'green'
    }
    
    async function deleteZP(){
        const URL = getURL('zonaspressao');
        let body = {
            id:id,
            sigla:sigla,
            descricao:descricao,
            tag_ft:tag_ft,
            tag_pt:tag_pt};
        const response = await window.fetch(URL, {
            method: 'DELETE',
            headers: {
            'content-type': 'application/json',
            },
            body: JSON.stringify(body),
        })
        
        onClick();
    }
    return(
        <Container>
            
            <Tag color={tagColorStr}></Tag> 
            <div>
                <span>{sigla}</span>
                <small>{descricao}</small>
            </div> 
            <div>
                <small>{tag_ft}</small>
                <small>{tag_pt}</small>
            </div> 
            <div>
                <input type="button" value="X" onClick={deleteZP}/>
            </div>              
            
        </Container>

    );
}


export default CardZp;