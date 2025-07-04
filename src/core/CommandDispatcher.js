// src/core/CommandDispatcher.js
import connectionManager from './ConnectionManager';
import deviceRegistry from './DeviceRegistry';
import { getWidgetByType } from './widgetRegistry'; // Імпортуємо наш реєстр

class CommandDispatcher {
  /**
   * Відправляє команду на MQTT брокер.
   * @param {string} entityId - ID сутності.
   * @param {any} value - Значення для відправки.
   * @param {string} [commandKey='default'] - Ключ команди, що відповідає опису в getCommandMappings.
   */
  dispatch({ entityId, value, commandKey = 'default' }) {
    const componentConfig = deviceRegistry.getEntity(entityId);
    if (!componentConfig) {
      console.error(`[CommandDispatcher] Component with ID "${entityId}" not found.`);
      return;
    }

    const widgetDef = getWidgetByType(componentConfig.type);
    if (!widgetDef?.getCommandMappings) {
      console.error(`[CommandDispatcher] No command mappings found for widget type "${componentConfig.type}".`);
      return;
    }

    const commandMappings = widgetDef.getCommandMappings(componentConfig);
    const targetTopic = commandMappings[commandKey];

    if (targetTopic) {
      console.log(`[CommandDispatcher] Dispatching to broker '${componentConfig.brokerId}'. Topic: '${targetTopic}', Value: '${value}'`);
      connectionManager.publishToTopic(
        componentConfig.brokerId,
        targetTopic,
        String(value)
      );
    } else {
      console.error(`[CommandDispatcher] No command topic found for entity "${entityId}" with commandKey "${commandKey}". Check widgetRegistry.`);
    }
  }
}

const commandDispatcher = new CommandDispatcher();
export default commandDispatcher;