import React from "react";
import { Container, 
    Tag } 
from "./styles";
import filters from '../../utils/filters';
interface ICardResultsProps{
    tagColor : boolean;
    title:string;
    subTitle:string;
    actualflowvalue: string;
    calculatedflowvalue: string;
    min: string;
    max: string;
    percentage: string;
}

const CardResults : React.FC<ICardResultsProps> = (
    {tagColor ,
    title,
    subTitle,
    actualflowvalue,
    calculatedflowvalue,
    min,
    max,
    percentage
}
) => {
    let tagColorStr = ''
    const tagType = filters(actualflowvalue, min,max)
    switch (tagType){
        case 'low':
            tagColorStr = 'blue';
            break;
        case 'ok':
            tagColorStr = 'green';
            break;
        case 'hi':
            tagColorStr = 'yellow';
            break;
        case 'hihi':
            tagColorStr = 'red';
            break;
    }
    return(
        <Container>
            <Tag color={tagColorStr}></Tag> 
            <div id="title">
                <span>{title}</span>
                <small>{subTitle}</small>
            </div> 
            <div id="info">
                <small>max: {max} l/s</small>
                <small>min: {min} l/s</small>
                <small>percentage: {percentage}%</small>
            </div> 
            <div id="vc">
                <small>VC: {calculatedflowvalue} l/s</small>
            </div>              
            <h3>VA: {actualflowvalue} l/s</h3>
        </Container>

    );
}


export default CardResults;