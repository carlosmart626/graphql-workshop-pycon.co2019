import React from 'react';
import ReactMarkdown from 'react-markdown';


class OrganizationHeader extends React.Component {
    render() {
        return (
            <div className="ui inverted vertical masthead center aligned segment">
                <div className="ui container">
                    <div className="ui large secondary inverted pointing menu">
                        <a className="active item">index</a>
                        <div className="right menu">
                            <a className="ui item">Inscribirse</a>
                        </div>
                    </div>
                </div>
                <div className="ui text container">
                    <h1 className="ui inverted header">
                        {this.props.organization.title}
                    </h1>
                    <ReactMarkdown source={this.props.organization.description}/>
                </div>
            </div>
        )
    }
}

export default OrganizationHeader