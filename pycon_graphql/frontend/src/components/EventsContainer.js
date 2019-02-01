import React from 'react';
import {Container, Header, Icon, Grid, GridColumn} from 'semantic-ui-react'
import ReactMarkdown from 'react-markdown';
import Leaflet from 'leaflet';
import MapContainer from './MapContainer'
import Moment from 'react-moment';


Leaflet.Icon.Default.imagePath = '//cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.0/images/';

const dateStyles = {
    marginRight: '4px',
    marginLeft: '4px',
};


class EventsContainer extends React.Component {
    render() {
        return (
            <Container>
                <Header
                    as='h4'
                    style={{
                        marginTop: '50px',
                    }}
                >Proximos Eventos!</Header>
                {this.props.events.map(({node}, idx) => (
                    <div key={idx}>
                        {console.log(node)}
                        {console.log("^^node")}
                        <Grid stackable divided>
                            <Grid.Row>
                                <Grid.Column width={10}>
                                    <Header as='h2' style={{ marginTop: '20px', }}>
                                        {node.title}
                                        <div className="sub header">
                                            <Icon name='calendar alternate outline'/>
                                            <Moment parse="YYYY-MM-DD" format="YYYY/MM/DD" style={dateStyles}>
                                                {node.eventDay}
                                            </Moment>
                                            de
                                            <Moment parse="HH:mm" format="hh:mm a" style={dateStyles}>
                                                {node.initialHour}
                                            </Moment>
                                            a
                                            <Moment parse="HH:mm" format="hh:mm a" style={dateStyles}>
                                                {node.endHour}
                                            </Moment>
                                        </div>
                                    </Header>

                                    <div>
                                        <ReactMarkdown source={node.description}/>
                                    </div>
                                </Grid.Column>
                                <Grid.Column width={6}>
                                    <MapContainer lat={node.latitude} lng={node.longitude} zoom={node.zoom} title={node.title}/>
                                </Grid.Column>
                            </Grid.Row>
                        </Grid>
                    </div>
                    ))
                }
            </Container>
        )
    }
}

export default EventsContainer;