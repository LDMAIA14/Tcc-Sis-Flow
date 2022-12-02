import styled from "styled-components";


export const Container = styled.div`
    height: 100vh;

    display: flex;
    flex: 1;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    background-color: ${props => props.theme.colors.primary};
`;

export const Logo = styled.div`
    display: flex;
    align-items: center;

    margin-bottom: 10px;

    >h2{
        color: ${props => props.theme.colors.white};
        margin-left: 7px;
    }

    >img{
        width: 80px;
        height: 80px;
        margin-right: 20px;
    }
    
`;

export const Form = styled.form`
    width: 400px;
    height: 350px;
    padding: 30px;
    border-radius: 10px;
    background-color: ${props => props.theme.colors.tertiary};;


`;

export const FormTitle = styled.div`
    margin-bottom: 40px;
    color: ${props => props.theme.colors.white};
    font-size: 30px;
    
    &::after{
        content: '';
        display: block;
        width: 55px;
        border-bottom: 10px solid ${props => props.theme.colors.warning};
    }

`;

