import React from 'react';
import ReactMarkdown from 'react-markdown';


const titleContainer = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '450px',
    marginTop: '-50px',
};

const titleText = {
    alignSelf: 'flex-center',
};


class OrganizationHeader extends React.Component {
    render() {
        const coverImage = this.props.organization.coverImage || '';
        return (
            <div className="ui inverted vertical masthead center aligned segment" style={{backgroundImage: `url(${coverImage})`}}>
                <div className="ui container">
                    <div className="ui large secondary inverted pointing menu">
                        <a className="active item">index</a>
                        <div className="right menu">
                            <a className="ui item">Inscribirse</a>
                        </div>
                    </div>
                </div>
                <div className="ui text container" style={titleContainer}>
                    <div style={titleText}>
                        <h1 className="ui inverted header">
                            {this.props.organization.title}
                        </h1>
                        <ReactMarkdown source={this.props.organization.description}/>
                    </div>
                </div>
            </div>
        )
    }
}

export default OrganizationHeader