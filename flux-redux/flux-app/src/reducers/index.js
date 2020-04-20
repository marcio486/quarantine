///Contem os reducers
import toDos from './toDo';
import { combineReducers } from 'redux';//combina todos os reducers em 1 import

export default combineReducers({
    toDos,
})