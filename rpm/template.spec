Name:           ros-indigo-pr2-navigation-perception
Version:        0.1.25
Release:        0%{?dist}
Summary:        ROS pr2_navigation_perception package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_navigation_perception
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-filters
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-laser-filters
Requires:       ros-indigo-laser-geometry
Requires:       ros-indigo-laser-tilt-controller-filter
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-pr2-machine
Requires:       ros-indigo-pr2-navigation-self-filter
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-semantic-point-annotator
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-filters
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-laser-filters
BuildRequires:  ros-indigo-laser-geometry
BuildRequires:  ros-indigo-laser-tilt-controller-filter
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-pr2-machine
BuildRequires:  ros-indigo-pr2-navigation-self-filter
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-semantic-point-annotator
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-topic-tools

%description
This package holds navigation-specific sensor configuration options and launch
files for the PR2.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Feb 06 2015 Devon Ash <dash@clearpathrobotics.com> - 0.1.25-0
- Autogenerated by Bloom

