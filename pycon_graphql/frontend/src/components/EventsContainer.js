import React from 'react';
import { Container, Header, Icon } from 'semantic-ui-react'
import ReactMarkdown from 'react-markdown';


class EventsContainer extends React.Component {
    render() {
        return (
            <Container>
                <Header
                    as='h2'
                    style={{
                        marginTop: '50px',
                      }}
                >Proximos Eventos!</Header>
                { this.props.events.map(({ node }, idx) => (
                    <div key={idx}>
                        {console.log(node)}
                        {console.log("^^node")}
                        <h3>
                            {node.title} <span><Icon name='calendar alternate outline'/> {node.eventDay}</span>
                        </h3>
                        <div>
                            <ReactMarkdown source={node.description}/>
                        </div>
                    </div>
                ))}
            </Container>
        )
    }
}

export default EventsContainer