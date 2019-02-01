import React from 'react';
import { gql } from 'apollo-boost';
import { Query } from 'react-apollo';
import ReactMarkdown from 'react-markdown';
import OrganizationHeader from './OrganizationHeader';
import EventsContainer from './EventsContainer';

const GET_EVENT = gql`
  query{
      events{
        edges{
          node{
            uuid
            title
            eventDay
            initialHour
            endHour
            description
          }
        }
      }
      organization{
        title
        description
      }
    }
`

const App = () => (
  <Query query={GET_EVENT}>
    {({ loading, error, data }) => {
      if (loading) return <div>Loading...</div>;
      if (error) return <div>Error :(</div>;

      const events = data.events.edges || [];
      const organization = data.organization || null;

      return (
          <div>
            <OrganizationHeader organization={organization}/>
            <EventsContainer events={events}/>
          </div>
      )
    }}
  </Query>
);

export default App;