import React from 'react';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';


class MapContainer extends React.Component {
    render() {
        // create an array with marker components
        const position = [this.props.lat, this.props.lng];
        return (
            <div className="map">
                <Map center={position} zoom={this.props.zoom} dragging={false} scrollWheelZoom={false}>
                    <TileLayer
                        attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <Marker position={position}>
                        <Popup>
                            {this.props.title}
                        </Popup>
                    </Marker>
                </Map>
            </div>
        );
    }
}

export default MapContainer