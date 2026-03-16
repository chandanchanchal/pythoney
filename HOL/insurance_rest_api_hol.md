# Hands-On Lab (HOL): Building REST APIs for an Insurance System

## 1. Objective

In this Hands-On Lab, learners will design and implement **5 REST APIs
for a basic Insurance Management System**.

By the end of this lab, learners should be able to:

-   Design REST API endpoints
-   Implement APIs using either:
    -   Java Spring Boot
    -   .NET Web API
-   Handle HTTP methods correctly
-   Use request/response models
-   Implement basic validation
-   Connect to a database (optional but recommended)
-   Test APIs using Postman or Swagger

------------------------------------------------------------------------

## 2. Business Scenario

An **Insurance company** wants to build a system to manage **customers
and their insurance policies**.

The system should allow:

-   Registering customers
-   Creating insurance policies
-   Viewing policies
-   Updating policy details
-   Submitting claims

You will build **5 REST APIs** to support these operations.

------------------------------------------------------------------------

## 3. Technology Options

Learners can use either stack.

### Option 1 --- Java Track

-   Java 17+
-   Spring Boot
-   Spring Web
-   Spring Data JPA
-   H2 / MySQL
-   Maven or Gradle

### Option 2 --- .NET Track

-   .NET 6 / .NET 7
-   ASP.NET Core Web API
-   Entity Framework Core
-   SQL Server / SQLite

------------------------------------------------------------------------

## 4. Data Model

### Customer

  Field        Type
  ------------ ---------
  customerId   Integer
  name         String
  email        String
  phone        String
  address      String

### Policy

  Field           Type
  --------------- ---------
  policyId        Integer
  policyType      String
  premiumAmount   Decimal
  startDate       Date
  endDate         Date
  customerId      Integer

### Claim

  Field         Type
  ------------- ---------
  claimId       Integer
  policyId      Integer
  claimAmount   Decimal
  claimDate     Date
  status        String

------------------------------------------------------------------------

## 5. REST APIs to Implement

Learners must implement the following **5 APIs**.

### API 1 --- Create Customer

**Endpoint**

    POST /api/customers

**Request Body**

``` json
{
  "name": "Rahul Sharma",
  "email": "rahul@gmail.com",
  "phone": "9876543210",
  "address": "Hyderabad"
}
```

**Response**

    201 Created

``` json
{
  "customerId": 1,
  "message": "Customer created successfully"
}
```

------------------------------------------------------------------------

### API 2 --- Create Insurance Policy

**Endpoint**

    POST /api/policies

**Request Body**

``` json
{
  "policyType": "Health",
  "premiumAmount": 12000,
  "startDate": "2025-01-01",
  "endDate": "2026-01-01",
  "customerId": 1
}
```

**Response**

``` json
{
  "policyId": 1001,
  "message": "Policy created successfully"
}
```

------------------------------------------------------------------------

### API 3 --- Get Policies by Customer

**Endpoint**

    GET /api/customers/{customerId}/policies

**Example**

    GET /api/customers/1/policies

**Response**

``` json
[
  {
    "policyId": 1001,
    "policyType": "Health",
    "premiumAmount": 12000
  },
  {
    "policyId": 1002,
    "policyType": "Vehicle",
    "premiumAmount": 8000
  }
]
```

------------------------------------------------------------------------

### API 4 --- Update Policy

**Endpoint**

    PUT /api/policies/{policyId}

**Request Body**

``` json
{
  "premiumAmount": 15000
}
```

**Response**

``` json
{
  "message": "Policy updated successfully"
}
```

------------------------------------------------------------------------

### API 5 --- Submit Insurance Claim

**Endpoint**

    POST /api/claims

**Request Body**

``` json
{
  "policyId": 1001,
  "claimAmount": 5000,
  "claimDate": "2025-03-15"
}
```

**Response**

``` json
{
  "claimId": 501,
  "status": "Submitted"
}
```

------------------------------------------------------------------------

## 6. Project Structure

### Java (Spring Boot)

Suggested packages:

    controller
    service
    repository
    model
    dto
    exception

Example:

    CustomerController
    PolicyController
    ClaimController
    CustomerService
    PolicyService
    CustomerRepository

### .NET Web API

Suggested folders:

    Controllers
    Services
    Repositories
    Models
    DTOs

Example:

    CustomerController.cs
    PolicyController.cs
    ClaimController.cs
    CustomerService.cs
    PolicyService.cs

------------------------------------------------------------------------

## 7. Validation Requirements

  Field           Rule
  --------------- ---------------
  email           must be valid
  premiumAmount   \> 0
  claimAmount     \> 0
  phone           10 digits

------------------------------------------------------------------------

## 8. Bonus Tasks (Optional)

If time permits, learners should also implement:

### Bonus 1

Add API:

    GET /api/policies/{policyId}

### Bonus 2

Add Claim Status Update

    PUT /api/claims/{claimId}

### Bonus 3

Add Swagger documentation

### Bonus 4

Add Exception handling

------------------------------------------------------------------------

## 9. Testing

Learners must test APIs using:

-   Postman
-   Swagger UI
-   Curl (optional)

Test cases should include:

-   Valid request
-   Invalid data
-   Missing fields
-   Non-existing ID

------------------------------------------------------------------------

## 10. Deliverables

Each learner should submit:

-   Source code
-   Postman collection
-   API documentation
-   Screenshots of working APIs

------------------------------------------------------------------------

## 11. Evaluation Criteria

  Criteria            Marks
  ------------------- -------
  API design          20
  Code structure      20
  Working endpoints   30
  Validation          10
  Testing             10
  Documentation       10
