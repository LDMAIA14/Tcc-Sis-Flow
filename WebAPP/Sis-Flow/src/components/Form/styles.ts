import styled from "styled-components";

export const Container = styled.form`
    width: 50%;
    height: 400px;
    margin:  10px 0;

    background-color: ${props=>props.color};
    color: ${props=>props.theme.colors.white};
    border-color: ${props=>props.theme.colors.white};
    border-width: 2px;
    border-radius: 7px;
    padding: 10px 20px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    >h2{
        margin-bottom: 30px;
    }
    >h2::after{
        content: '';
        display: block;
        width: 100%;
        border-bottom: 10px solid ${props=>props.theme.colors.success};
    }
    >input{
        width: 80%;
        height: 40px;
        border-radius: 5px;
        margin-top: 15px;
        text-align: center;
        font-size: 18px;

    }
    #Btn{
        margin-top: 25px;
        background-color: ${props=>props.theme.colors.success};
        color: ${props=>props.theme.colors.black};
    }
    >input:hover{
        transition-duration: 1s;
        opacity: .3;
    }
`;