export default function toDos(state = [],action) {
    //Action = objeto que vem da action toDo.js Ex: {type : 'ADD_TODO',text : 'texto'}
    switch (action.type) {
        case 'ADD_TODO':
            return [ ...state,{ 
                id:Math.floor(Math.random() * 100),
                text: action.text
            }]
        case 'REM_TODO':
            for (let index = 0; index < state.length; index++) { 
                
                
                if (state[index].id === parseInt(action.id)){
                    console.log(state)
                    state.splice(index,1)
                    const next_state = state
                    console.log(state)
                    return next_state
                }
            }     
        break
        default:
            return state;
    }
}
