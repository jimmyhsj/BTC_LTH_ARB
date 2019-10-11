import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';


class BtcArb extends React.Component {
    render() {
        return (
            <div class="flex-center position-ref full-height">
                <div class="top-right links">
                </div>
                <div class="content">
                    <div class="title m-b-md">
                        Laravel
                    </div>
                </div>
            </div>
        );
    }
}

ReactDOM.render(
    <BtcArb/>,
    document.getElementById('root')
);