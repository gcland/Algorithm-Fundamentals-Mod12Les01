# Case Study: Optimizing Text Messaging App with Efficient Data Structures


#1 and #3 - Messaging / Conversation List Management

# dictionary allows management of various variables including time, sender, message ID(which could preserve order), message, etc. (any further tags). 
# Message Search: For each dictionary (message history with any given recipient) would force the search to search each dictionary within the list of messages)
# this complexity of search is simple. See search example below.
# 
# 
# messages = {} 
# { message-recipientID : [{ messageID: '', timestamp: '', sender: '', message: 'message1'} , { messageID2: '', timestamp2: '', sender: '', message2: 'message2'} }

messageList = []
# Note: keys in dictionary below are a "userID" and represent a separate conversation between someone or a group of people
messages = { 

    1: messageList,
    2: messageList,
    3: messageList
            
            }
message1 = { 
    'messageID' : '1', 
    'timestamp' : '', 
    'sender' : '',
    'message' : 'c'
      }

message2 = { 
    'messageID' : '2', 
    'timestamp' : '', 
    'sender' : '',
    'message' : 'a'
      }

message3 = { 
    'messageID' : '3', 
    'timestamp' : '', 
    'sender' : '',
    'message' : 'b'
      }

message4 = { 
    'messageID' : '4', 
    'timestamp' : '', 
    'sender' : '',
    'message' : 'a'
      }
messages[1].append(message1)
messages[1].append(message2)
messages[1].append(message3)
messages[1].append(message4)
# print(messages)


searchItem = 'c'

# Initially linear O(n), becomes more complex the more conversations searched
# Search becomes quadratic (O(n^2)) if searching every conversation (for conversation in messages /n for message in conversation /n (remainder of code))
for message in messages[1]:
    if message['message'] == searchItem:
        print(message['message'], message['messageID'])

# Arrays: do not offer ability to store additional information within the message system. Ordered by stack. Ordered by index (key / ID?)
# 
# Linked List: allow messages to be linked by next. Ordered by stack / index (key / ID). Search time can be O(n)
#
# Hash table is allows data to be stored in key value pairs, similar to dictionary. 
# - Searching in hash table could be similar to searching in dicitonary; 
# - search a given recipient ID, search each str within a list of strings within the message index.
# - if well organized, time to serach can be O(1) (The dictionary above was set up like a hash table)

# Tree is nonlinear data structure (compared to linear structure of lists/dictionary)
# - Allows faster search by seraching sets to see if element is present
# - Data is evenly distributed. Search time can be O(log n)


#2

# Polling:
#A communications technique that determines when a terminal is ready to send data.

# Long polling:
# Takes HTTP request/response polling and increases efficiency since repeated requests can waste resources
# Long polling the server holds the client connection open for as long as possible 
# More resource intensive than WebSocket
# Comes with latency issues because gateways can remain open for a long time
# 

# Web Sockets:
# Bidirectional communication between web client and web server over a persistent single connection. The connection
# - is kept alive as long as needed.
# Less resource intensive
# Keeps connection open while eliminating latency issues
# Messaging is supported on both client and server; client and server and stream messages to each other independently