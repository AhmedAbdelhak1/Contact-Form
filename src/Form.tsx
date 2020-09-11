import React from 'react';
import './Form.css';

function Form() {
    return (
        <form className="formarea">
                <div className="container">
                    <label >FullName:</label>
                    <input type="text"/>
                    <label >Email:</label>
                    <input type="email" name="email" id=""/>
                    <label >Subject:</label>
                    <input type="text"/>
                    <label >Message:</label>
                    <textarea name="" ></textarea>
                    <button className="btn" type="submit">Send It</button>
                </div>
            

        </form>
    )
}

export default Form;
