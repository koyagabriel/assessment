## System Design
### Layered (n-tier) Architecture:
This pattern can be used to structure programs that can be decomposed into groups of subtasks, each of which is at a particular level of abstraction. Each layer provides services to the next higher layer. <br />

The most commonly found 4 layers of a general information system are as follows.
- Presentation layer (also known as UI layer)
- Application layer (also known as service layer)
- Business logic layer (also known as domain layer)
- Data access layer (also known as persistence layer)

The advantage of a layered architecture is the separation of concerns, which means that each layer can focus solely on its role.

#### Best for:

- New applications that need to be built quickly
- Enterprise or business applications that need to mirror traditional IT departments and processes.
- Teams with inexperienced developers who don’t understand other architectures yet
- Applications requiring strict maintainability and testability standards

### Event Driven Architecture:
This pattern primarily deals with events and has 4 major components; event source, event listener, channel and event bus. Sources publish messages to particular channels on an event bus. Listeners subscribe to particular channels. Listeners are notified of messages that are published to a channel to which they have subscribed before.
This is very different from the layered architecture where all data will typically pass through all layers.

#### Best for:
- Asynchronous systems with asynchronous data flow

### MVC Architecture:
This is done to separate internal representations of information from the ways information is presented to, and accepted from, the user. It decouples components and allows efficient code reuse.

#### Best for:
- Building for World Wide Web applications in major programming languages.
- Web frameworks such as Django and Rails.
- same as layered architecture.

### Service Oriented Architecture:
A service-oriented architecture (SOA) is a style of software design where services are provided to the other components by application components, through a communication protocol over a network.

### MicroService Architecture:
It is a variant of the service-oriented architecture (SOA) architectural style that structures an application as a collection of loosely coupled services.
