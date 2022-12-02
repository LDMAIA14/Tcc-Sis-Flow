const getURL = (endpoint:string):string => {
    const ip = '127.0.0.1'
    switch(endpoint) { 
        case 'login': { 
           return "http://" + ip + ":8080/sis-flow/api/v1/login"; 
          
        } 
        case 'currentvalues': { 
            return "http://" + ip + ":8080/sis-flow/api/v1/currentvalues";  
        
        } 
        case 'results': { 
            return "http://" + ip + ":8080/sis-flow/api/v1/resultados";  
        
        } 
        case 'zonaspressao': { 
            return "http://" + ip + ":8080/sis-flow/api/v1/zonapressao";  
        
        } 
        case 'dashboard': { 
            return "http://" + ip + ":8080/sis-flow/api/v1/dashboard";  
        
        } 
        default: { 
           //statements; 
           return "none";  
        } 
    } 
}



export default getURL;