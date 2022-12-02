import React, {createContext, useState, useContext, ReactNode} from "react";
import getURL from "../utils/getURL";

interface ChildrenProps{
    children: React.ReactNode;
}

interface IAuthContext{
    logged: boolean;
    permission:string;
    name:string
    signIn(email: string, password: string): void;
    signOut():void;

}

const AuthContext = createContext<IAuthContext>({}as IAuthContext);


const AuthProvider: React.FC<ChildrenProps> = ({children}) =>{
    const [logged,setLogged] = useState<boolean>(()=>{
        const isLogged = localStorage.getItem('@user-sisflow:logged');

        return !!isLogged;
    });
    const [permission,setPermission] = useState<string>(()=>{
        const perm = localStorage.getItem('@user-sisflow:permission');
        if(perm===null){
            return '';
        }
        return perm;
    });
    const [name, setName] = useState<string>('');

    const signIn = (email:string, password:string) => {
        
        SignPost(email,password).then(d => {
           
            if(d.response === 'true'){
                setName(d.name);
                setPermission(d.permissao)
                localStorage.setItem('@user-sisflow:logged', 'true');
                localStorage.setItem('@username-sisflow:logged', d.name);
                localStorage.setItem('@user-sisflow:permission', d.permissao);
                setLogged(true);
            }else{
                setName('');
                localStorage.setItem('@username-sisflow:logged', '');
                localStorage.setItem('@user-sisflow:permission', '');
                alert('Senha ou Login estão incorretos')
            }
        }) 
    }


    const signOut = () => {
        localStorage.removeItem('@user-sisflow:logged');
        localStorage.removeItem('@username-sisflow:logged');
        localStorage.removeItem('@user-sisflow:permission');
        setLogged(false);
        setPermission('');
    }

    return(
        <AuthContext.Provider value={{logged,name,permission, signIn, signOut}}>
            {children}
        </AuthContext.Provider>

    )
}

function useAuth():IAuthContext{
    const context = useContext(AuthContext);

    return context;
}



async function SignPost(email:string,password:string) {
    
    let URL = getURL('login');
    let body = {user:email,
        pwd:password};
    const response = await window.fetch(URL, {
        method: 'POST',
        headers: {
        'content-type': 'application/json',
        },
        body: JSON.stringify(body),
    })

    const txt = await response.text()
    if (response.ok) {
        const Resposta = txt
        if (Resposta){
            return JSON.parse(Resposta)
        }else{
            return Promise.reject(new Error(`Sem Resposta`))
        }
    }else{
        const error = new Error("error")
        return Promise.reject(error)
    }
}



export {AuthProvider, useAuth};