// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from moveit_msgs:msg/ObjectColor.idl
// generated code does not contain a copyright notice
#include "moveit_msgs/msg/detail/object_color__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `id`
#include "rosidl_runtime_c/string_functions.h"
// Member `color`
#include "std_msgs/msg/detail/color_rgba__functions.h"

bool
moveit_msgs__msg__ObjectColor__init(moveit_msgs__msg__ObjectColor * msg)
{
  if (!msg) {
    return false;
  }
  // id
  if (!rosidl_runtime_c__String__init(&msg->id)) {
    moveit_msgs__msg__ObjectColor__fini(msg);
    return false;
  }
  // color
  if (!std_msgs__msg__ColorRGBA__init(&msg->color)) {
    moveit_msgs__msg__ObjectColor__fini(msg);
    return false;
  }
  return true;
}

void
moveit_msgs__msg__ObjectColor__fini(moveit_msgs__msg__ObjectColor * msg)
{
  if (!msg) {
    return;
  }
  // id
  rosidl_runtime_c__String__fini(&msg->id);
  // color
  std_msgs__msg__ColorRGBA__fini(&msg->color);
}

bool
moveit_msgs__msg__ObjectColor__are_equal(const moveit_msgs__msg__ObjectColor * lhs, const moveit_msgs__msg__ObjectColor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->id), &(rhs->id)))
  {
    return false;
  }
  // color
  if (!std_msgs__msg__ColorRGBA__are_equal(
      &(lhs->color), &(rhs->color)))
  {
    return false;
  }
  return true;
}

bool
moveit_msgs__msg__ObjectColor__copy(
  const moveit_msgs__msg__ObjectColor * input,
  moveit_msgs__msg__ObjectColor * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  if (!rosidl_runtime_c__String__copy(
      &(input->id), &(output->id)))
  {
    return false;
  }
  // color
  if (!std_msgs__msg__ColorRGBA__copy(
      &(input->color), &(output->color)))
  {
    return false;
  }
  return true;
}

moveit_msgs__msg__ObjectColor *
moveit_msgs__msg__ObjectColor__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  moveit_msgs__msg__ObjectColor * msg = (moveit_msgs__msg__ObjectColor *)allocator.allocate(sizeof(moveit_msgs__msg__ObjectColor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(moveit_msgs__msg__ObjectColor));
  bool success = moveit_msgs__msg__ObjectColor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
moveit_msgs__msg__ObjectColor__destroy(moveit_msgs__msg__ObjectColor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    moveit_msgs__msg__ObjectColor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
moveit_msgs__msg__ObjectColor__Sequence__init(moveit_msgs__msg__ObjectColor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  moveit_msgs__msg__ObjectColor * data = NULL;

  if (size) {
    data = (moveit_msgs__msg__ObjectColor *)allocator.zero_allocate(size, sizeof(moveit_msgs__msg__ObjectColor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = moveit_msgs__msg__ObjectColor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        moveit_msgs__msg__ObjectColor__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
moveit_msgs__msg__ObjectColor__Sequence__fini(moveit_msgs__msg__ObjectColor__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      moveit_msgs__msg__ObjectColor__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

moveit_msgs__msg__ObjectColor__Sequence *
moveit_msgs__msg__ObjectColor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  moveit_msgs__msg__ObjectColor__Sequence * array = (moveit_msgs__msg__ObjectColor__Sequence *)allocator.allocate(sizeof(moveit_msgs__msg__ObjectColor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = moveit_msgs__msg__ObjectColor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
moveit_msgs__msg__ObjectColor__Sequence__destroy(moveit_msgs__msg__ObjectColor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    moveit_msgs__msg__ObjectColor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
moveit_msgs__msg__ObjectColor__Sequence__are_equal(const moveit_msgs__msg__ObjectColor__Sequence * lhs, const moveit_msgs__msg__ObjectColor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!moveit_msgs__msg__ObjectColor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
moveit_msgs__msg__ObjectColor__Sequence__copy(
  const moveit_msgs__msg__ObjectColor__Sequence * input,
  moveit_msgs__msg__ObjectColor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(moveit_msgs__msg__ObjectColor);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    moveit_msgs__msg__ObjectColor * data =
      (moveit_msgs__msg__ObjectColor *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!moveit_msgs__msg__ObjectColor__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          moveit_msgs__msg__ObjectColor__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!moveit_msgs__msg__ObjectColor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
