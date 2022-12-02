import React from "react";
import logoImg from '../../assets/pipes-pipe-svgrepo-com.svg';
import { Container,
        Header,
        LogImg,
        MenuContainer,
        MenuItemLink,
        MenuItemButton,
        Title 
    } from "./styles";

import {
    MdDashboard,
    MdExitToApp,
    MdReviews,
    MdAddTask,
    MdAccountTree
} from 'react-icons/md';

import { useAuth } from "../../hooks/auth";


const Aside: React.FC = () =>{
    const {signOut} = useAuth();
    return(
        <Container>
            <Header>
                <LogImg src={logoImg} alt="Sistema de Predicao de Vazão"/>
                <Title>Sis Flow</Title>

            </Header>
        
            <MenuContainer>
                <MenuItemLink href="/dashboard">
                    <MdDashboard/> Dashboard
                </MenuItemLink>
                <MenuItemLink href="/list/resultados">
                    <MdReviews/> Resultados
                </MenuItemLink>
                <MenuItemLink href="/list/currentvalues">
                    <MdAddTask/> Valores Atuais
                </MenuItemLink>
                <MenuItemLink href="/zonaspressao">
                    <MdAccountTree/> Zonas de Abastecimento
                </MenuItemLink>
                <MenuItemButton onClick = {signOut}>
                    <MdExitToApp/>Sair
                </MenuItemButton>
            </MenuContainer>
        </Container>
    );
}

export default Aside;