import {combineReducers} from 'redux'
import socketSlice from './Socket/socketSlice';
const rootReducer = combineReducers({socketSlice})

export default rootReducer;