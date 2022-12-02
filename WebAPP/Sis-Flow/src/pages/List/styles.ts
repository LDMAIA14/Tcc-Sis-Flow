import styled from "styled-components";


export const Container = styled.div``;   

export const Content = styled.main``;   

export const Filters = styled.div`
    width: 100%;
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
    .tag-filter{
        font-size: 18px;
        font-weight: 500;
        background: none;
        color: ${props => props.theme.colors.white};
        
        margin: 0 10%;

        transition: opacity .3s;
        opacity: .25;
        :hover{
            opacity: 0.7;
        }

        
        
    }
    .tag-filter-low::after{
            content: '';
            display: block;
            width: 55px;
            margin: 0 auto;
            border-bottom: 10px solid blue;
    }
    .tag-filter-ok::after{
            content: '';
            display: block;
            width: 55px;
            margin: 0 auto;
            border-bottom: 10px solid green;
    }
    .tag-filter-hi::after{
        content: '';
        display: block;
        width: 55px;
        margin: 0 auto;
        border-bottom: 10px solid yellow;
    }
    .tag-filter-hihi::after{
            content: '';
            display: block;
            width: 55px;
            margin: 0 auto;
            border-bottom: 10px solid red;
    }

    .tag-actived{
        opacity: 1;
    }
`;                      