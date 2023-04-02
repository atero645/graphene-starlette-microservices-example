const { ApolloServer } = require('apollo-server');
const { ApolloGateway, IntrospectAndCompose } = require("@apollo/gateway");

const gateway = new ApolloGateway({

  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'users', url: 'http://users-service/' },
      { name: 'tasks', url: 'http://tasks-service/' },
      // ...additional subgraphs...
    ]
  })
});

const server = new ApolloServer({
  gateway,

  // Currently, subscriptions are enabled by default with Apollo Server, however,
  // subscriptions are not compatible with the gateway.  We hope to resolve this
  // limitation in future versions of Apollo Server.  Please reach out to us on
  // https://spectrum.chat/apollo/apollo-server if this is critical to your adoption!
  subscriptions: false,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});