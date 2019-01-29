import React from 'react';
import { gql } from 'apollo-boost';
import { Query } from 'react-apollo';

const GET_DOG = gql`
  query{
      events{
        edges{
          node{
            uuid
            title
            eventDay
            initialHour
            endHour
          }
        }
      }
    }
`

const App = () => (
  <Query query={GET_DOG}>
    {({ loading, error, data }) => {
      if (loading) return <div>Loading...</div>;
      if (error) return <div>Error :(</div>;

      const events = data.events.edges || [];

      return (
          <div>
          { events.map(({ node }, idx) => (
            <div key={idx}>
              <h3>
                {node.title} <span>{node.eventDay}</span>
              </h3>
            </div>
          ))}
          </div>
      )
    }}
  </Query>
);

export default App;