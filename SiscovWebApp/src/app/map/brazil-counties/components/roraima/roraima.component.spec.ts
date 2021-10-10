import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RoraimaComponent } from './roraima.component';

describe('RoraimaComponent', () => {
  let component: RoraimaComponent;
  let fixture: ComponentFixture<RoraimaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RoraimaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RoraimaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
