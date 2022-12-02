import React, {useMemo, useState, useEffect} from "react";

import ContentHeader from "../../components/ContentHeader";




import { v4 as uuidv4 } from 'uuid';

import {Container, 
    Content
} from './styles';
import getURL from "../../utils/getURL";
import Form from "../../components/Form";
import CardZp from "../../components/CardZp";

interface IZpProps{
    idzonapressao: string;
    sigla:string;
    descricao: string; 
    tag_ft: string;
    tag_pt: string;
}

const Zps: React.FC = () =>{

    const [zonasabastecimento,setZonasAbastecimento] = useState<IZpProps[]>([]);
    
    useEffect(()=>{
        getData();

    },[]);
    function refresh(){
        getData()
    }
    function getData(){
        const URL = getURL('zonaspressao');    
        fetch(URL).then(res=>{
            res.json().then(data=>{
                console.log(data)
                setZonasAbastecimento(data);
            });
        }
        );

    }
    return(

        <Container>
            <ContentHeader title={'Zonas de Abastecimento'} lineColor={'#771022'}>
                    
            </ContentHeader>
            
            <Content>
                <Form onSubit={refresh}/>
                {
                    zonasabastecimento.map(item=>{
                        return(
                            <CardZp 
                                key={item.idzonapressao}
                                id={item.idzonapressao}
                                tagColor={false}
                                sigla={item.sigla}
                                descricao={item.descricao}
                                tag_ft={item.tag_ft}
                                tag_pt={item.tag_pt}
                                onClick={refresh}
                            />
                        )
                    })
                }
            </Content>
        </Container>

    );
   
}

export default Zps;