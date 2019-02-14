# Security

### Expectation
The Developer is adept at implementing both transport and message level security in web applications. They should also have an understanding of the Application Security Verification Standard (OWASP).

### Justification
Web services typically ensures security by using two ways to implement security in applications and they include:

1. **Transport level security** is a security protocol based on the Secure Sockets layer or Transport layer security (SSL/TLS) which runs beneath the HTTP protocol which is the underlying protocol used by the World Wide Web and this protocol defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands. SSL/TLS provides security features such as authentication, data protection and cryptographic token support to secure HTTP connections.
2. **Message Level Security**  is an application layer service and facilitates the protection of data between applications by sending security information along with the message/data been sent. For example, a portion of the message may be signed by a sender and encrypted for a particular receiver. Message level security doesn’t utilise SSL/TSL and is intended to work between applications. It’s most commonly used today by chatting applications and email providers.

The OWASP application verification standard is an open source standard for ensuring secure measures/practices when building applications and some of these practices which I currently adhere to in my day to day tasks typically include:

**Input Validation or data validation**: it is the proper testing of any input supplied by a user or application. This prevents improperly formed data from entering the application. I ensure validating user inputs on my current engagement.

**Output Encoding**: this involves converting sensitive information from the server into a safe form where the input is displayed as safe data to the user. 

**Access Control** involves authentication and authorisation of users. This is two fold, Authentication requires managing user sessions and access to the application whereas Authorisation involves giving authenticated users different access levels to different parts of the application. I ensure that when building secure and robust I implement authentication by use of JWT tokens.

**Error Handling and Logging** involves having an error handling strategy that does not involve logging sensitive or unusable information.

