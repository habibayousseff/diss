// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from moveit_task_constructor_msgs:srv/GetSolution.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "moveit_task_constructor_msgs/srv/get_solution.h"


#ifndef MOVEIT_TASK_CONSTRUCTOR_MSGS__SRV__DETAIL__GET_SOLUTION__STRUCT_H_
#define MOVEIT_TASK_CONSTRUCTOR_MSGS__SRV__DETAIL__GET_SOLUTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetSolution in the package moveit_task_constructor_msgs.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Request
{
  uint32_t solution_id;
} moveit_task_constructor_msgs__srv__GetSolution_Request;

// Struct for a sequence of moveit_task_constructor_msgs__srv__GetSolution_Request.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Request__Sequence
{
  moveit_task_constructor_msgs__srv__GetSolution_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} moveit_task_constructor_msgs__srv__GetSolution_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'solution'
#include "moveit_task_constructor_msgs/msg/detail/solution__struct.h"

/// Struct defined in srv/GetSolution in the package moveit_task_constructor_msgs.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Response
{
  moveit_task_constructor_msgs__msg__Solution solution;
} moveit_task_constructor_msgs__srv__GetSolution_Response;

// Struct for a sequence of moveit_task_constructor_msgs__srv__GetSolution_Response.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Response__Sequence
{
  moveit_task_constructor_msgs__srv__GetSolution_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} moveit_task_constructor_msgs__srv__GetSolution_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  moveit_task_constructor_msgs__srv__GetSolution_Event__request__MAX_SIZE = 1
};
// response
enum
{
  moveit_task_constructor_msgs__srv__GetSolution_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/GetSolution in the package moveit_task_constructor_msgs.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Event
{
  service_msgs__msg__ServiceEventInfo info;
  moveit_task_constructor_msgs__srv__GetSolution_Request__Sequence request;
  moveit_task_constructor_msgs__srv__GetSolution_Response__Sequence response;
} moveit_task_constructor_msgs__srv__GetSolution_Event;

// Struct for a sequence of moveit_task_constructor_msgs__srv__GetSolution_Event.
typedef struct moveit_task_constructor_msgs__srv__GetSolution_Event__Sequence
{
  moveit_task_constructor_msgs__srv__GetSolution_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} moveit_task_constructor_msgs__srv__GetSolution_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEIT_TASK_CONSTRUCTOR_MSGS__SRV__DETAIL__GET_SOLUTION__STRUCT_H_
