# APIs

### Expectation
The Developer should be able to design and build complex APIs using a number of protocols (REST, XML-RPC) taking into account backwards compatibility while being able to easily implement new features.


### Justification
My current engagement uses a microservice architecture which exposes me todifferent complex APIs built with different technologies ranging from ruby on rails, flask and node. I have been part of the development team that spun all these services from scratch. In a microservice environment, making an API backward compatible is important as this allow clients that uses a particular service to continue working as expected while we improve this service. We have been able to achieve this by using stable URI, stable representations, and API versioning.

A restful apis are built using the representational state transfer architectural style and typically combines HTTP verbs such as GET, PUT, POST, PATCH and DELETE and matching uri to match and locate resources, responses are usually in JSON which is less verbose to XML since it can be easily serialised by browsers which run on javascript.

[Click to view rails api](https://github.com/koyagabriel/Ruby_Alpha_Blog)


[Click to view flask api](https://github.com/koyagabriel/urlshortener/tree/front-end-design/app/api)

RPC stands for Remote Procedure Calls and XML-RPC basically allows client execute procedures on a remote server and get responses using XML as the messaging envelope.