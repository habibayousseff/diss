// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from moveit_task_constructor_msgs:msg/TaskDescription.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "moveit_task_constructor_msgs/msg/task_description.hpp"


#ifndef MOVEIT_TASK_CONSTRUCTOR_MSGS__MSG__DETAIL__TASK_DESCRIPTION__TRAITS_HPP_
#define MOVEIT_TASK_CONSTRUCTOR_MSGS__MSG__DETAIL__TASK_DESCRIPTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "moveit_task_constructor_msgs/msg/detail/task_description__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stages'
#include "moveit_task_constructor_msgs/msg/detail/stage_description__traits.hpp"

namespace moveit_task_constructor_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TaskDescription & msg,
  std::ostream & out)
{
  out << "{";
  // member: task_id
  {
    out << "task_id: ";
    rosidl_generator_traits::value_to_yaml(msg.task_id, out);
    out << ", ";
  }

  // member: stages
  {
    if (msg.stages.size() == 0) {
      out << "stages: []";
    } else {
      out << "stages: [";
      size_t pending_items = msg.stages.size();
      for (auto item : msg.stages) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskDescription & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: task_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_id: ";
    rosidl_generator_traits::value_to_yaml(msg.task_id, out);
    out << "\n";
  }

  // member: stages
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.stages.size() == 0) {
      out << "stages: []\n";
    } else {
      out << "stages:\n";
      for (auto item : msg.stages) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskDescription & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace moveit_task_constructor_msgs

namespace rosidl_generator_traits
{

[[deprecated("use moveit_task_constructor_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const moveit_task_constructor_msgs::msg::TaskDescription & msg,
  std::ostream & out, size_t indentation = 0)
{
  moveit_task_constructor_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use moveit_task_constructor_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const moveit_task_constructor_msgs::msg::TaskDescription & msg)
{
  return moveit_task_constructor_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<moveit_task_constructor_msgs::msg::TaskDescription>()
{
  return "moveit_task_constructor_msgs::msg::TaskDescription";
}

template<>
inline const char * name<moveit_task_constructor_msgs::msg::TaskDescription>()
{
  return "moveit_task_constructor_msgs/msg/TaskDescription";
}

template<>
struct has_fixed_size<moveit_task_constructor_msgs::msg::TaskDescription>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<moveit_task_constructor_msgs::msg::TaskDescription>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<moveit_task_constructor_msgs::msg::TaskDescription>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOVEIT_TASK_CONSTRUCTOR_MSGS__MSG__DETAIL__TASK_DESCRIPTION__TRAITS_HPP_
