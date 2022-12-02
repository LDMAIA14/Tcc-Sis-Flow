const formatDate = (date:string): string =>{
    const dateFormatted = new Date(date);

    const year = dateFormatted.getFullYear();

    const day = (dateFormatted.getDate()+1) < 10 ? `0${(dateFormatted.getDate()+1)}` : (dateFormatted.getDate()+1);
    
    
    const month = (dateFormatted.getMonth()+1) < 10 ? `0${(dateFormatted.getMonth()+1)}` : (dateFormatted.getMonth()+1);
    

    return `${day}/${month}/${year}`
};

export default formatDate;