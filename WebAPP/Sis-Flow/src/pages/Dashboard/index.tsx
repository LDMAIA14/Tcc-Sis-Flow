import React, {useMemo, useState, useEffect} from "react";
import { Container, Content } from "./styles";

import listOfMonth from "../../utils/month";
import listOfYear from "../../utils/years";

import ContentHeader from "../../components/ContentHeader";
import SelectInput from "../../components/SelectInput";
import BoxData from "../../components/BoxData";
import getURL from "../../utils/getURL";


interface IResults{

    low:string;
    ok:string;
    hi:string;
    hihi:string;
}

const Dashboard: React.FC = () =>{
    const [monthSelected, setMonthSelected] = useState<number>(new Date().getMonth() + 1);
    const [yearSelected, setYearSelected] = useState<number>(new Date().getFullYear());
    const [results,setResults] = useState<IResults>({'low':'0','ok':'0','hi':'0','hihi':'0'});
    
    useEffect(()=>{
       
        dashboardDidMount();
         
    },[])

    useMemo(()=>{
        dashboardDidMount();

    },[monthSelected,yearSelected]);

    const years = useMemo(()=>{
        return listOfYear.map((year,index)=>{
            return {
                value: year,
                label: year,
            }
        });
        
    },[]);
    const months = useMemo(()=>{
        return listOfMonth.map((month,index)=>{
            return {
                value: index+1,
                label: month,
            }
        });
        
    
    },[]);
    async function dashboardDidMount(){
        const URL = getURL('dashboard');
        let body = {
            month:monthSelected,
            year:yearSelected
        };
        const response = await window.fetch(URL, {
            method: 'POST',
            headers: {
            'content-type': 'application/json',
            },
            body: JSON.stringify(body),
        })
        
        if(response.ok){      
            const data = await response.text();   
            const myJson = JSON.parse(data.replaceAll("'",'"').replaceAll('[','').replace(']','')) 
            
            setResults(myJson)
            console.log(results)
        }
        else{
            return Promise.reject(new Error(`Sem Resposta`))
        }
          
    }

    


    const handleMonthSelected = (month:string)=>{
        try{
            const parseMonth = Number(month);
            setMonthSelected(parseMonth);
        }catch(error){
            throw new Error('invalid month value. It is acept values from 0 - 11');
            
        }
    }
    const handleYearSelected = (year:string)=>{
        try{
            const parseYear = Number(year);
            setYearSelected(parseYear);
        }catch(error){
            throw new Error('invalid year value. It is acept integer number.');
            
        }
    }
    const date = new Date();
    return (
        <Container>
            <ContentHeader title="Dashboard" lineColor="#F7931B">
                <SelectInput options={months} onChange={(e) => handleMonthSelected(e.target.value)} defaultValue={monthSelected}/>
                <SelectInput options={years} onChange={(e) => handleYearSelected(e.target.value)} defaultValue={yearSelected}/>
            </ContentHeader>    
            <Content>
                <BoxData
                    title="Resultados Abaixo da Curva"
                    amount={parseInt(results.low)}
                    footerlabel={"atualizado: " + date.toLocaleString() }
                    icon="low"
                    color="#131b81"
                
                />
                <BoxData
                    title="Valores Dentro da Curva"
                    amount={parseInt(results.ok)}
                    footerlabel={"atualizado: " +  date.toLocaleString()}
                    icon="ok"
                    color="#15ca3c"
                
                />
                <BoxData
                    title="Valores Acima da Curva Até 10%"
                    amount={parseInt(results.hi)}
                    footerlabel={"atualizado: " +  date.toLocaleString()}
                    icon="hi"
                    color="#a7a538"
                
                />
                <BoxData
                    title="Valores Acima da Curva HIHI"
                    amount={parseInt(results.hihi)}
                    footerlabel={"atualizado: " +  date.toLocaleString()}
                    icon="hihi"
                    color="#a5140a"
                
                />

            </Content>
        </Container>
        
    );
}

export default Dashboard;