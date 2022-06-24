import { Module } from '@nestjs/common';
import { ObdController } from './controllers/obd/obd.controller';

@Module({
  imports: [],
  controllers: [ObdController],
  providers: [],
})
export class AppModule {}
