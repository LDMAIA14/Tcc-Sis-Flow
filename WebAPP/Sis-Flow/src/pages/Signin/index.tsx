import React , { useState } from "react";
import { Container,
        Logo,
        Form,
        FormTitle
     } from "./styles";

import logoImg from '../../assets/pipes-pipe-svgrepo-com.svg'
import Input from "../../components/Input";
import Button from "../../components/Button";


import {useAuth} from '../../hooks/auth';

const Signin: React.FC = () =>{
    const [email, setEmail] = useState<string>('');
    const [password, setPassWord] = useState<string>('');

    const {signIn} = useAuth();

    return (
        <Container>
            <Logo>
                <img src={logoImg} alt=""/>
                <h2>Sis-Flow</h2>
            </Logo>
            <Form onSubmit={(e)=> { 
                e.preventDefault();
                signIn(email,password)}}>
                <FormTitle>Entrar</FormTitle>
                <Input 
                    required
                    type="email"
                    placeholder="e-mail"
                    onChange={(e)=> setEmail(e.target.value)}
                />
                <Input 
                    required
                    type="password"
                    placeholder="password"
                    onChange={(e)=> setPassWord(e.target.value)}
                />
                <Button type="submit" >Acessar</Button>
                
            </Form>
        </Container>
    );
}

export default Signin;