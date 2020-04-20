export function addToDo(text){
    return {
        type: 'ADD_TODO',
        text,
    };
}

export function RemoveToDo(id){
    return {
        type: 'REM_TODO',
        id,
    };
}