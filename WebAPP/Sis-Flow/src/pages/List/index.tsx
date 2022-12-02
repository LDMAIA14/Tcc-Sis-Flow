import React, {useMemo, useState, useEffect} from "react";
import { useParams } from 'react-router-dom';
import ContentHeader from "../../components/ContentHeader";
import CardCurrentValue from "../../components/CardCurrentValue";




import { v4 as uuidv4 } from 'uuid';

import {Container, 
    Content, 
    Filters
} from './styles';
import getURL from "../../utils/getURL";
import filters from "../../utils/filters";
import CardResults from "../../components/CardResults";

interface IData{
    id:string;
    tagname: string;
    description: string;
    flow: string;
    result:string;
    standartdeviation:string
    tagColor:boolean;
}

interface IResults{
    TagName:string;
    Value:string;
    TimeStamp:string;
    Descricao:string;
    tag_ft:string;
    datahora:string;
    valor_calculado:string;
    valor_atual:string;
    max_calculado:string;
    min_calculado:string;
    descricao:string;
    percentage_value:string;
    sigla:string;

}


const List: React.FC = () =>{
    
    const [deviationFilterSelected, setdeviationFilterSelected] = useState(['low','ok','hi','hihi']);
   
    const [results, setResults] = useState<IResults[]>([]);
    const [filteredResults, setFilteredResults] = useState<IResults[]>([]);
    
    
    const pageTitle = useParams().type;
    
    const titleOptions = useMemo(() => {
       
        return pageTitle === 'resultados' ? 
        {title: 'Resultados', lineColor:"#110d99"} : 
        {title: 'Valores Correntes', lineColor:"#E44C4E"}
    }, [pageTitle]);

    

    useMemo(()=>{
        try{
            sortData();
        }catch{
                
        }
        
        return 0;
    },[deviationFilterSelected,results])
   

    useEffect(()=>{
        if(pageTitle==='currentvalues'){            
            cvDidMount();
            setInterval(()=>{
                cvDidMount()
            },30000);
        }
        if(pageTitle==='resultados'){            
            resultsDidMount();
            setInterval(()=>{
                resultsDidMount()
            },30000);
        }
        
    },[])
    

    async function cvDidMount(){
        const URL = getURL('currentvalues');

        const response = await window.fetch(URL, {
            method: 'GET',
            headers: {
            'content-type': 'application/json',
            },
        })
          
        if(response.ok){      
            const data = await response.text();   
            const myJson = JSON.parse(data.replaceAll("'",'"')) 
            
            setResults(myJson)
        }
        else{
            return Promise.reject(new Error(`Sem Resposta`))
        }
          
    }
    async function resultsDidMount(){
        const URL = getURL('results');

        const response = await window.fetch(URL, {
            method: 'GET',
            headers: {
            'content-type': 'application/json',
            },
        })
          
        if(response.ok){      
            const data = await response.text();   
            const myJson = JSON.parse(data.replaceAll("'",'"')) 
            
            setResults(myJson);
            sortData();
        }
        else{
            return Promise.reject(new Error(`Sem Resposta`))
        }
          
    }
    const handleFrequencyClick = (type:string = 'test') =>{
     
        const alreadySelected = deviationFilterSelected.findIndex(item => item === type);
       
        if(alreadySelected>=0){
            const filtered = deviationFilterSelected.filter(field => field !== type);
            setdeviationFilterSelected(filtered);
        }else{
            setdeviationFilterSelected((prev)=> [...prev,type]);
        }       
    }
   
    function sortData(){
        const res = [... results.filter(item => {
            let type = filters(item.valor_atual, item.min_calculado,item.max_calculado)
            const isSelected = deviationFilterSelected.findIndex(item => item === type );

            if (isSelected >=0){
                return true;
            }else{
                return false;
            }
        })];
        
        const sortedData = [...res.sort(comparer)]
        setFilteredResults(sortedData);
        
    }
    
    function comparer(a:IResults, b:IResults) {
        let percentA = parseFloat(a.percentage_value);
        let percentB = parseFloat(b.percentage_value);
        let typeA = filters(a.valor_atual, a.min_calculado,a.max_calculado)
        let typeB = filters(b.valor_atual, b.min_calculado,b.max_calculado)
        let codA = defineCodeFilterLevel(typeA);
        let codB = defineCodeFilterLevel(typeB);
        if(codA<codB){return 1}
        if(codA>codB){return -1}
        if(percentA<percentB){return 1}
        if(percentA>percentB){return -1}
        
        return 0;
    }
    function defineCodeFilterLevel(type:string){
        let code = -1
        switch (type){
            case 'low':
                code = 1;
                break;
            case 'ok':
                code = 2;
                break;
            case 'hi':
                code = 3;
                break;
            case 'hihi':
                code = 4;
                break;
        }
        return code
    }
    if(pageTitle === 'resultados'){
        return (
            <Container>
                <ContentHeader title={titleOptions.title} lineColor={titleOptions.lineColor}>
                    
                </ContentHeader>
                
                <Filters>
                    <button 
                        type="button"
                        className={`tag-filter tag-filter-low
                        ${deviationFilterSelected.includes('low') && 'tag-actived'}
                        `}
                        onClick={()=>handleFrequencyClick('low')}
                    >
                        LOW
                    </button>
                    <button 
                        type="button"
                        className={`tag-filter tag-filter-ok
                        ${deviationFilterSelected.includes('ok') && 'tag-actived'}
                        `}
                        onClick={()=>handleFrequencyClick('ok')}
                    >
                        OK
                    </button>
                    <button 
                        type="button"
                        className={`tag-filter tag-filter-hi
                        ${deviationFilterSelected.includes('hi') && 'tag-actived'}
                        `}
                        onClick={()=>handleFrequencyClick('hi')}
                    >
                        HI
                    </button>
                    <button 
                        type="button"
                        className={`tag-filter tag-filter-hihi
                        ${deviationFilterSelected.includes('hihi') && 'tag-actived'}
                        `}
                        onClick={()=>handleFrequencyClick('hihi')}
                    >
                        HIHI
                    </button>
                </Filters>
                   
                
                <Content>
                {
                    
                    filteredResults.map(item=>{
                        var title='';
                        var subTitle ='';
                        var value='';
                        var date=new Date();
                        { 
                            date = new Date(item.datahora);
                            title= item.sigla + ' - ' + item.descricao;
                            subTitle=item.datahora;
                            var va = parseFloat(item.valor_atual)
                            var vc = parseFloat(item.valor_calculado)
                            var percent = ((va / vc)*100).toFixed(2)
                            value = parseFloat(item.valor_atual).toFixed(2)
                            return(
                                <CardResults 
                                    key={String(uuidv4())}
                                    tagColor={false}
                                    title={title}
                                    subTitle={subTitle}
                                    actualflowvalue={value}
                                    calculatedflowvalue={parseFloat(item.valor_calculado).toFixed(2)}
                                    min={item.min_calculado}
                                    max={item.max_calculado}
                                    percentage={item.percentage_value}
                                />
                            )    
                        }
                    })
                }
                </Content>        
            </Container>
    
        );
    }
    if(pageTitle === 'currentvalues'){
        return (
            <Container>
                <ContentHeader title={titleOptions.title} lineColor={titleOptions.lineColor}>
                    
                </ContentHeader>
                
                <Filters>
                    
                </Filters>
                   
                
                <Content>
                {
                    
                    results.map(item=>{
                        var title='';
                        var subTitle ='';
                        var value='';
                        var date=new Date();
                        { 
                            date = new Date(item.TimeStamp);
                            title= item.TagName;
                            subTitle=item.Descricao
                            value = parseFloat(item.Value).toFixed(2)
                            return(
                                <CardCurrentValue 
                                    key={String(uuidv4())}
                                    tagColor={false}
                                    title={title}
                                    subTitle={subTitle}
                                    flowValue={value}
                                />
                            )
                        }
                        
                    })
                }
                </Content>        
            </Container>
    
        );
       
    }
    
    return <Content/>;
    
}

export default List;