import React from "react";
import { Container, 
    Tag } 
from "./styles";

interface ICardCurrentValueProps{
    tagColor : boolean;
    title:string;
    subTitle:string;
    flowValue: string;
}

const CardCurrentValue : React.FC<ICardCurrentValueProps> = (
    {tagColor ,
    title,
    subTitle,
    flowValue}
) => {
    let tagColorStr = ''
    if(tagColor===true){
        tagColorStr = 'red'
    }else{
        tagColorStr = 'green'
    }
    return(
        <Container>
            <Tag color={tagColorStr}></Tag> 
            <div>
                <span>{title}</span>
                <small>{subTitle}</small>
            </div>               
            <h2>{flowValue} l/s</h2>
        </Container>

    );
}


export default CardCurrentValue;