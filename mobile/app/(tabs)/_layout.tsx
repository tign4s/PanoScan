import { Tabs } from 'expo-router';
import React from 'react';

import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';
import { Ionicons } from '@expo/vector-icons';

export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors.primary,
        tabBarInactiveTintColor: Colors.secondary,
        tabBarStyle: {height: 60},
        tabBarLabelStyle: {marginBottom: 10},
        tabBarActiveBackgroundColor: Colors.white,
        headerShown: false,
      }}>
      <Tabs.Screen
        name="photo"
        options={{
          title: 'Photo',
          tabBarLabel: 'Photo',
          tabBarIcon: ({ color, size }) => (
            <Ionicons name='camera-sharp' color={color} size={size}/>
          ),
        }}
      />
      <Tabs.Screen
        name="history"
        options={{
          title: 'Historique',
          tabBarLabel: 'Historique',
          tabBarIcon: ({color, size}) => 
            <Ionicons name="images" color={color} size={size}/>,
        }}
      />
    </Tabs>
  );
}
