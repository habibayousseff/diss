// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from moveit_msgs:msg/DisplayTrajectory.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "moveit_msgs/msg/detail/display_trajectory__rosidl_typesupport_introspection_c.h"
#include "moveit_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "moveit_msgs/msg/detail/display_trajectory__functions.h"
#include "moveit_msgs/msg/detail/display_trajectory__struct.h"


// Include directives for member types
// Member `model_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `trajectory`
#include "moveit_msgs/msg/robot_trajectory.h"
// Member `trajectory`
#include "moveit_msgs/msg/detail/robot_trajectory__rosidl_typesupport_introspection_c.h"
// Member `trajectory_start`
#include "moveit_msgs/msg/robot_state.h"
// Member `trajectory_start`
#include "moveit_msgs/msg/detail/robot_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  moveit_msgs__msg__DisplayTrajectory__init(message_memory);
}

void moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_fini_function(void * message_memory)
{
  moveit_msgs__msg__DisplayTrajectory__fini(message_memory);
}

size_t moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__size_function__DisplayTrajectory__trajectory(
  const void * untyped_member)
{
  const moveit_msgs__msg__RobotTrajectory__Sequence * member =
    (const moveit_msgs__msg__RobotTrajectory__Sequence *)(untyped_member);
  return member->size;
}

const void * moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_const_function__DisplayTrajectory__trajectory(
  const void * untyped_member, size_t index)
{
  const moveit_msgs__msg__RobotTrajectory__Sequence * member =
    (const moveit_msgs__msg__RobotTrajectory__Sequence *)(untyped_member);
  return &member->data[index];
}

void * moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_function__DisplayTrajectory__trajectory(
  void * untyped_member, size_t index)
{
  moveit_msgs__msg__RobotTrajectory__Sequence * member =
    (moveit_msgs__msg__RobotTrajectory__Sequence *)(untyped_member);
  return &member->data[index];
}

void moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__fetch_function__DisplayTrajectory__trajectory(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const moveit_msgs__msg__RobotTrajectory * item =
    ((const moveit_msgs__msg__RobotTrajectory *)
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_const_function__DisplayTrajectory__trajectory(untyped_member, index));
  moveit_msgs__msg__RobotTrajectory * value =
    (moveit_msgs__msg__RobotTrajectory *)(untyped_value);
  *value = *item;
}

void moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__assign_function__DisplayTrajectory__trajectory(
  void * untyped_member, size_t index, const void * untyped_value)
{
  moveit_msgs__msg__RobotTrajectory * item =
    ((moveit_msgs__msg__RobotTrajectory *)
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_function__DisplayTrajectory__trajectory(untyped_member, index));
  const moveit_msgs__msg__RobotTrajectory * value =
    (const moveit_msgs__msg__RobotTrajectory *)(untyped_value);
  *item = *value;
}

bool moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__resize_function__DisplayTrajectory__trajectory(
  void * untyped_member, size_t size)
{
  moveit_msgs__msg__RobotTrajectory__Sequence * member =
    (moveit_msgs__msg__RobotTrajectory__Sequence *)(untyped_member);
  moveit_msgs__msg__RobotTrajectory__Sequence__fini(member);
  return moveit_msgs__msg__RobotTrajectory__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_member_array[3] = {
  {
    "model_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(moveit_msgs__msg__DisplayTrajectory, model_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "trajectory",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(moveit_msgs__msg__DisplayTrajectory, trajectory),  // bytes offset in struct
    NULL,  // default value
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__size_function__DisplayTrajectory__trajectory,  // size() function pointer
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_const_function__DisplayTrajectory__trajectory,  // get_const(index) function pointer
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__get_function__DisplayTrajectory__trajectory,  // get(index) function pointer
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__fetch_function__DisplayTrajectory__trajectory,  // fetch(index, &value) function pointer
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__assign_function__DisplayTrajectory__trajectory,  // assign(index, value) function pointer
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__resize_function__DisplayTrajectory__trajectory  // resize(index) function pointer
  },
  {
    "trajectory_start",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(moveit_msgs__msg__DisplayTrajectory, trajectory_start),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_members = {
  "moveit_msgs__msg",  // message namespace
  "DisplayTrajectory",  // message name
  3,  // number of fields
  sizeof(moveit_msgs__msg__DisplayTrajectory),
  false,  // has_any_key_member_
  moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_member_array,  // message members
  moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_init_function,  // function to initialize message memory (memory has to be allocated)
  moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_type_support_handle = {
  0,
  &moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_members,
  get_message_typesupport_handle_function,
  &moveit_msgs__msg__DisplayTrajectory__get_type_hash,
  &moveit_msgs__msg__DisplayTrajectory__get_type_description,
  &moveit_msgs__msg__DisplayTrajectory__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_moveit_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, moveit_msgs, msg, DisplayTrajectory)() {
  moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, moveit_msgs, msg, RobotTrajectory)();
  moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, moveit_msgs, msg, RobotState)();
  if (!moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_type_support_handle.typesupport_identifier) {
    moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &moveit_msgs__msg__DisplayTrajectory__rosidl_typesupport_introspection_c__DisplayTrajectory_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
