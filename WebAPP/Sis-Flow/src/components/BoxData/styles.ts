import styled, { StyledComponent } from "styled-components";

interface IContainerProps{
    color:string;
}


export const Container = styled.div<IContainerProps>`
    width: 400px;
    height: 300px;
    margin:  10px 20px;
    opacity: 0.9;
    background-color: ${props=>props.color};
    color: ${props=>props.theme.colors.white};

    border-radius: 7px;
    padding: 10px 20px;

    position: relative;
    overflow: hidden;


    >img{
        height: 110%;
        position: absolute;
        top: -10px;
        right: -30px;
        opacity: .2;
        
    }
    >p{
        
        font-size:100px;
        font-weight:bold;
        margin: 30px 20px;

    }
    >span{
        font-size: 28px;
        font-weight: 500;

    }
    >small{
        font-size: 16px;
        position: absolute;
        bottom:10px;

        font-weight:bold;
    }
`;


export const Content = styled.div`
    

`;