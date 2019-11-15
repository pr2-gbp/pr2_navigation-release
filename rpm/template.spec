Name:           ros-melodic-pr2-navigation-global
Version:        0.1.28
Release:        1%{?dist}
Summary:        ROS pr2_navigation_global package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_navigation_global
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-amcl
Requires:       ros-melodic-joint-trajectory-generator
Requires:       ros-melodic-move-base
Requires:       ros-melodic-pr2-machine
Requires:       ros-melodic-pr2-move-base
Requires:       ros-melodic-pr2-navigation-config
Requires:       ros-melodic-pr2-tuck-arms-action
Requires:       ros-melodic-topic-tools
BuildRequires:  ros-melodic-catkin

%description
This package holds XML files for running the

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Nov 15 2019 David Feil-Seifer <dave@cse.unr.edu> - 0.1.28-1
- Autogenerated by Bloom

