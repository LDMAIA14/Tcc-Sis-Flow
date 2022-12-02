import React from 'react';
import {Container} from './styles'
import CountUp from 'react-countup';


import ok from '../../assets/ok_1.svg'
import low from '../../assets/ok_1.svg'
import hi from '../../assets/error_1.svg'
import hihi from '../../assets/error_1.svg'

interface IBoxDataProps{
    title:string;
    amount:number;
    footerlabel:string;
    icon:'low' | 'ok' | 'hi' | 'hihi'
    color:string
}


const BoxData: React.FC<IBoxDataProps> = ({title, amount, footerlabel, icon, color})=>{

    const iconSelected = ()=>{
        switch(icon){
            case 'low':
                return low;
            case 'ok':
                return ok;
            case 'hi':
                return hi;
            case 'hihi':
                return hihi;
            default:
                return undefined;
        }
    }

    return(
        <Container color={color}>
            <span>{title}</span>
            <p>
                <CountUp
                    end={amount}
                    separator="."
                    decimal=','
                    decimals={0}
                
                />
            </p>
            <small>{footerlabel}</small>
            <img src={iconSelected()} alt={title}/>
        </Container>
    )
}


export default BoxData;