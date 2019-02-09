import React from 'react';
import { render } from 'react-dom';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';
import gql from "graphql-tag";
import App from './components/App';
import './styles/styles.scss'

// Pass your GraphQL endpoint to uri
const client = new ApolloClient({ uri: 'http://localhost:8000/graphql' });

const ApolloApp = () => (
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);

render(<ApolloApp />, document.getElementById('app'));